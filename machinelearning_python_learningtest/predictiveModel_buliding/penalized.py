from math import sqrt

def normalize(list):
    mean = []
    std = []
    s = list.shape
    n_rows = s[0]
    n_cols = s[1]
    for j in range(n_cols):
        j_mean = sum([list[k][j] for k in range(n_rows)]) / n_rows
        mean.append(j_mean)
        coldiff = [(list[k][j] - j_mean) for k in range(n_rows)]
        std_val = sum(coldiff[i] * coldiff[i] for i in range(n_rows))
        std.append(sqrt(std_val / n_rows))

    norm_list = []
    for i in range(n_rows):
        row_norm = [(list[i][j] - mean[j]) / std[j] for j in range(n_cols)]
        norm_list.append(row_norm)

    return norm_list



def lars(x, y):
    n_rows = len(x)
    n_cols = len(x[0])

    beta = [0.0] * n_cols
    beta_matrix = []
    beta_matrix.append(list(beta))

    steps = 350
    step_size = 0.004
    nzlist = []
    for step in range(steps):
        residuals = [0.0] * n_rows
        for i in range(n_rows):
            y_pre = sum([x[i][k] * beta[k] for k in range(n_cols)])
            residuals[i] = y[i][0] - y_pre

        corr = [0.0] * n_cols
        for j in range(n_cols):
            corr[j] = sum([x[k][j] * residuals[k] for k in range(n_rows)]) / n_rows

        i_star = 0
        corr_star = corr[0]
        for j in range(1, n_cols):
            if abs(corr_star) < abs(corr[j]):
                i_star, corr_star = j, corr[j]

        beta[i_star] = step_size * corr_star / abs(corr_star)
        beta_matrix.append(list(beta))

        nz_beta = [index for index in range(n_cols) if beta[index] != 0]
        for q in nz_beta:
            if q not in nzlist:
                nzlist.append(q)

    return beta_matrix
# Выбираем самые полезные параметры 


def go_correlations(X, col):
    # Рассчитываем корреляцию всех признаков 
    go_correlations = X.corr()[col].abs().sort_values()

    # Отбираем признаки с корреляцией больше 0.1 
    gl_high_info_features = go_correlations[go_correlations > 0.1]

    print('Информативные признаки (есть связь):')
    gl_high_info_features = gl_high_info_features.drop([col, 'index'], errors='ignore')


    #Для финальной модели оставляем только информативные параметры  
    gl_final_param = gl_high_info_features.index.unique().tolist() 

    print(go_correlations.sort_values(ascending=False).head(20))

def calcular_metricas(VP, VN, FP, FN):
    N = VP + VN + FP + FN
    
    sensibilidade = VP / (VP + FN) if (VP + FN) > 0 else 0
    especificidade = VN / (FP + VN) if (FP + VN) > 0 else 0
    acuracia = (VP + VN) / N if N > 0 else 0
    precisao = VP / (VP + FP) if (VP + FP) > 0 else 0
    f_score = (2 * (precisao * sensibilidade) / (precisao + sensibilidade)) if (precisao + sensibilidade) > 0 else 0
    
    return {
        "Sensibilidade": round(sensibilidade, 4),
        "Especificidade": round(especificidade, 4),
        "Acurácia": round(acuracia, 4),
        "Precisão": round(precisao, 4),
        "F-score": round(f_score, 4)
    }

# Exemplo com os valores VP=50, VN=35, FP=5, FN=10
resultado = calcular_metricas(50, 35, 5, 10)
print(resultado)

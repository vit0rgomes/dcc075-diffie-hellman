"""
DCC075 - Segurança em Sistemas de Computação
Atividade 08 - Troca de Chaves de Diffie-Hellman (DH)

Descrição:
Implementação do protocolo Diffie-Hellman para estabelecimento de chave secreta
compartilhada (s) sobre um canal público inseguro.

Variáveis do Protocolo:
- p : Número primo público grande
- g : Raiz primitiva módulo p (pública)
- a : Chave privada de Alice (secreta)
- b : Chave privada de Bob (secreta)
- A : Chave pública de Alice -> A = (g^a) mod p
- B : Chave pública de Bob   -> B = (g^b) mod p
- s : Segredo compartilhado  -> s = (B^a) mod p = (A^b) mod p = g^(a*b) mod p

Como executar:
    python diffie_hellman.py
"""

import math


def eh_primo(n: int) -> bool:
    """Verifica se n é um número primo."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    for d in range(3, int(math.isqrt(n)) + 1, 2):
        if n % d == 0:
            return False
    return True


def fatores_primos(n: int) -> set[int]:
    """Retorna o conjunto de fatores primos distintos de n."""
    fatores = set()
    d = 2
    while d * d <= n:
        while n % d == 0:
            fatores.add(d)
            n //= d
        d += 1
    if n > 1:
        fatores.add(n)
    return fatores


def eh_raiz_primitiva(g: int, p: int) -> bool:
    """
    Verifica se g é raiz primitiva módulo p.
    Pelo critério algébrico: g é raiz primitiva mod p se e somente se,
    para todo fator primo q de (p - 1), g^((p - 1) / q) mod p != 1.
    """
    phi = p - 1
    for q in fatores_primos(phi):
        if pow(g, phi // q, p) == 1:
            return False
    return True


if __name__ == "__main__":
    # 1. Parâmetros públicos (p primo grande e g raiz primitiva módulo p)
    p = 1000003  # Primo grande (> 1.000.000)
    g = 2        # Menor raiz primitiva módulo 1000003

    # Validação matemática de p e g
    assert eh_primo(p), f"Erro: p={p} não é primo!"
    assert eh_raiz_primitiva(g, p), f"Erro: g={g} não é raiz primitiva módulo {p}!"

    # 2. Chaves privadas escolhidas secretamente por Alice (a) e Bob (b)
    a = 345678   # Segredo privado de Alice (1 < a < p-1)
    b = 789123   # Segredo privado de Bob   (1 < b < p-1)

    # 3. Cálculo das chaves públicas enviadas pelo canal público
    # Alice calcula A = g^a mod p
    A = pow(g, a, p)

    # Bob calcula B = g^b mod p
    B = pow(g, b, p)

    # 4. Cálculo do segredo compartilhado (s)
    # Alice recebe B de Bob e calcula: s_alice = B^a mod p
    s_alice = pow(B, a, p)

    # Bob recebe A de Alice e calcula: s_bob = A^b mod p
    s_bob = pow(A, b, p)

    print("=" * 65)
    print("       PROTOCOLO DIFFIE-HELLMAN (COMPARTILHAMENTO DE SEGREDO)")
    print("=" * 65)
    print("1. PARÂMETROS PÚBLICOS:")
    print(f"   p (número primo)          = {p}")
    print(f"   g (raiz primitiva mod p)  = {g}")
    print("-" * 65)
    print("2. CHAVES PRIVADAS (SECRETAS):")
    print(f"   a (chave privada Alice)   = {a}")
    print(f"   b (chave privada Bob)     = {b}")
    print("-" * 65)
    print("3. CHAVES PÚBLICAS CALCULADAS (TROCADAS NA REDE):")
    print(f"   A = g^a mod p (Alice)     = {A}")
    print(f"   B = g^b mod p (Bob)       = {B}")
    print("-" * 65)
    print("4. SEGREDO COMPARTILHADO FINAL (s):")
    print(f"   s calculado por Alice (B^a mod p) = {s_alice}")
    print(f"   s calculado por Bob   (A^b mod p) = {s_bob}")
    print("=" * 65)

    assert s_alice == s_bob, "Erro: Os segredos calculados não coincidem!"
    print(f"[SUCESSO] Segredo compartilhado estabelecido com sucesso: s = {s_alice}")

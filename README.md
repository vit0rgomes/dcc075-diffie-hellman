# DCC075 - Segurança em Sistemas de Computação
## Atividade 08 - Protocolo de Troca de Chaves Diffie-Hellman (DH)

Implementação em Python do protocolo de troca de chaves **Diffie-Hellman**, desenvolvido para demonstrar o estabelecimento seguro de uma chave compartilhada através de um canal de comunicação inseguro sem que o segredo seja transmitido diretamente.

---

### Fundamentação Teórica

O protocolo Diffie-Hellman baseia-se na dificuldade do **Problema do Logaritmo Discreto (DLP)** em corpos finitos.

1. **Parâmetros Públicos:**
   - $p$: Número primo grande.
   - $g$: Raiz primitiva módulo $p$ (gerador do grupo cíclico multiplicativo $\mathbb{Z}_p^*$).
   - O código valida formalmente $g$ verificando se, para todo fator primo $q$ de $(p - 1)$:
     $$g^{\frac{p - 1}{q}} \not\equiv 1 \pmod{p}$$

2. **Geração dos Segredos Privados:**
   - Alice escolhe uma chave privada secreta $a$ tal que $1 < a < p - 1$.
   - Bob escolhe uma chave privada secreta $b$ tal que $1 < b < p - 1$.

3. **Cálculo e Troca das Chaves Públicas:**
   - Alice calcula sua chave pública e envia pela rede:
     $$A = g^a \pmod{p}$$
   - Bob calcula sua chave pública e envia pela rede:
     $$B = g^b \pmod{p}$$

4. **Derivação do Segredo Compartilhado:**
   - Alice recebe $B$ e calcula:
     $$s_{\text{Alice}} = B^a \pmod{p} = (g^b)^a \pmod{p} = g^{ab} \pmod{p}$$
   - Bob recebe $A$ e calcula:
     $$s_{\text{Bob}} = A^b \pmod{p} = (g^a)^b \pmod{p} = g^{ab} \pmod{p}$$
   - Ambos chegam ao mesmo valor $s = s_{\text{Alice}} = s_{\text{Bob}}$ sem que nenhum espião consiga derivar $a$, $b$ ou $s$ apenas observando $p$, $g$, $A$ e $B$ no canal.

---

### Parâmetros Utilizados na Simulação

- **Primo público ($p$):** `1000003` (primo $> 1.000.000$)
- **Raiz primitiva pública ($g$):** `2` (validada algebricamente)
- **Chave privada de Alice ($a$):** `345678`
- **Chave privada de Bob ($b$):** `789123`
- **Chave pública de Alice ($A$):** `354970`
- **Chave pública de Bob ($B$):** `564136`
- **Segredo compartilhado ($s$):** `968266`

---

### Como Executar

O projeto requer apenas o interpretador padrão Python 3.

```bash
# Execução direta:
python diffie_hellman.py

# No Windows via Python Launcher:
py diffie_hellman.py
```

---

### Exemplo de Saída

```text
=================================================================
       PROTOCOLO DIFFIE-HELLMAN (COMPARTILHAMENTO DE SEGREDO)
=================================================================
1. PARÂMETROS PÚBLICOS:
   p (número primo)          = 1000003
   g (raiz primitiva mod p)  = 2
-----------------------------------------------------------------
2. CHAVES PRIVADAS (SECRETAS):
   a (chave privada Alice)   = 345678
   b (chave privada Bob)     = 789123
-----------------------------------------------------------------
3. CHAVES PÚBLICAS CALCULADAS (TROCADAS NA REDE):
   A = g^a mod p (Alice)     = 354970
   B = g^b mod p (Bob)       = 564136
-----------------------------------------------------------------
4. SEGREDO COMPARTILHADO FINAL (s):
   s calculado por Alice (B^a mod p) = 968266
   s calculado por Bob   (A^b mod p) = 968266
=================================================================
[SUCESSO] Segredo compartilhado estabelecido com sucesso: s = 968266
```

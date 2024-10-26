#include <stdio.h>

// Função para verificar se um número pertence à sequência de Fibonacci
int pertenceFibonacci(int num) {
    if (num == 0 || num == 1) return 1;

    int a = 0, b = 1, c;
    while (b < num) {
        c = a + b;
        a = b;
        b = c;
    }

    return (b == num);
}

int main() {
    int numero;

    printf("Informe um numero: ");
    scanf("%d", &numero);

    if (pertenceFibonacci(numero)) {
        printf("O numero %d pertence a sequencia de Fibonacci.\n", numero);
    } else {
        printf("O numero %d nao pertence a sequencia de Fibonacci.\n", numero);
    }

    return 0;
}

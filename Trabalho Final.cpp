#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Pessoa {
    int codigo;
    char nome[50];
    char rua[50];
    char bairro[50];
    char cidade[50];
    char estado[3];
    char cep[10];
    char celular[15];
    char email[50];
    char cpf[15];
    char rg[15];
};

void adicionarPessoa(FILE *arquivo, struct Pessoa *p) {
    fwrite(p, sizeof(struct Pessoa), 1, arquivo);
}

void exibirPessoas(FILE *arquivo) {
    rewind(arquivo);

    struct Pessoa p;
    while (fread(&p, sizeof(struct Pessoa), 1, arquivo) == 1) {
        printf("Código: %d\n", p.codigo);
        printf("Nome: %s\n", p.nome);
        printf("Rua: %s\n", p.rua);
        printf("Bairro: %s\n", p.bairro);
        printf("Cidade: %s\n", p.cidade);
        printf("Estado: %s\n", p.estado);
        printf("CEP: %s\n", p.cep);
        printf("Celular: %s\n", p.celular);
        printf("E-mail: %s\n", p.email);
        printf("CPF: %s\n", p.cpf);
        printf("RG: %s\n", p.rg);
        printf("\n");
    }
}

int main() {
    FILE *arquivo;
    arquivo = fopen("pessoas.dat", "ab+"); 

    if (arquivo == NULL) {
        perror("Erro ao abrir o arquivo");
        return 1;
    }

    struct Pessoa pessoa;

    pessoa.codigo = 1;
    strcpy(pessoa.nome, "Fulano de Tal");
    strcpy(pessoa.rua, "Rua Principal");
    strcpy(pessoa.bairro, "Centro");
    strcpy(pessoa.cidade, "Cidade");
    strcpy(pessoa.estado, "SP");
    strcpy(pessoa.cep, "12345-678");
    strcpy(pessoa.celular, "987654321");
    strcpy(pessoa.email, "fulano@example.com");
    strcpy(pessoa.cpf, "123.456.789-01");
    strcpy(pessoa.rg, "123456789");

    adicionarPessoa(arquivo, &pessoa);

    exibirPessoas(arquivo);

    fclose(arquivo);

    return 0;
}

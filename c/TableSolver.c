#include <stdlib.h>
#include "TableSolver.h"

/*************************************************
 * 
 * IMPLEMENTAÇÃO DA INTERFACE DO TAD LISTA
 * 
 *************************************************/
lista cria_lista(){
    lista lst = (tcabec *)malloc(sizeof(tcabec));
    lst->primeiro = NULL;
    lst->ultimo = NULL;
    lst->tamanho = 0;
    return lst;
}

int len_lista(lista lst){
    return lst->tamanho;
}

tdado prim_lista(lista lst){
    return lst->primeiro->dado;
}

tdado ult_lista(lista lst){
    return lst->ultimo->dado;
}

lista append_lista(lista lst, tdado dado){
    if(lst == NULL) return NULL;

    pnoh novoNo = (pnoh)malloc(sizeof(tnode));
    novoNo->proximo = NULL;
    novoNo->dado = dado;

    if(lst->tamanho == 0){
        lst->primeiro = novoNo;
        lst->ultimo = novoNo;
    }
    else {
        lst->ultimo->proximo = novoNo;
        lst->ultimo = novoNo;
    }
    lst->tamanho++;
    return lst;
}

tdado dado_lista(lista lst, int pos) {
    int contpulos;
    pnoh no_corrente;

    if((lst == NULL) || (pos < 0) || (pos >= lst->tamanho)) 
        return NULL;

    contpulos = 0;
    no_corrente = lst->primeiro;
    while(contpulos != pos){
        contpulos++;
        no_corrente = no_corrente->proximo;
    }
    return no_corrente->dado;
}

int index_lista(lista lst, tdado dado) {
    int tamanho = lst->tamanho;

    for(int posicao=0; posicao < tamanho; posicao++){
        if(dado_lista(lst,posicao) == dado)
            return posicao;
    }
    return -1;
}

lista insert_lista(lista lst, int index, tdado dado){
    int cont_pulos;
    pnoh no_certo;
    pnoh no_anterior;

    // Verificando erros
    if((lst == NULL) || (index < 0)){
        return NULL;
    }

    // Criando novo nó 
    pnoh novo_no = (pnoh)malloc(sizeof(tnode));
    novo_no->dado = dado;

    // Setando valores padrão para as variáveis
    cont_pulos = 0;
    no_anterior = lst->primeiro;

    // Caso seja na primeira posição
    if(index == 0){
        novo_no->proximo = lst->primeiro;
        lst->primeiro = novo_no;
        lst->tamanho++;

    }else if(index >= lst->tamanho){
        append_lista(lst, dado);
    }
    else{
        // Pulando até encontrar a posição anterior
        while(cont_pulos != (index - 1)){
            cont_pulos++;
            no_anterior = no_anterior->proximo;
        }
        // Posição correta
        no_certo = no_anterior->proximo;

        //Colocando novo item entre o nó anterior e o nó certo
        novo_no->proximo = no_certo;
        no_anterior->proximo = novo_no;

        // Aumentando o tamanho da lista
        lst->tamanho++;
    }
    

}

tdado remove_lista(lista lst, int index){
    int cont_pulos;
    pnoh no_certo;
    pnoh no_anterior;

    if((lst == NULL) || (index < 0) || (index >= lst->tamanho)){
        return NULL;
    }

    // Setando valores padrão para as variáveis
    cont_pulos = 0;
    no_anterior = lst->primeiro;

    if(index == 0){
        // Caso seja o primeiro item ele executa uma sequencia de códigos menor e atualiza no cabeçalho da lista o primeiro item
        no_certo = lst->primeiro;
        lst->primeiro = no_certo->proximo;

    } else{
        // Pulando até encontrar o nó da posição anterior
        while(cont_pulos != (index - 1)){
            cont_pulos++;
            no_anterior = no_anterior->proximo;
        }

        // Faz as alterações necessárias retirando o nó selecionado da sequencia na lista
        no_certo = no_anterior->proximo;
        no_anterior->proximo = no_certo->proximo;

        // Caso seja o último item ele atualiza no cabeçalho da lista o último item
        if( index == (lst->tamanho - 1)){
            lst->ultimo = no_anterior;
        }

    }

    // Diminuindo o tamanho da lista e libertando o espaço que estava alocado
    lst->tamanho--;
    return no_certo->dado;
    free(no_certo);
}

// Lista insertLista(Lista lst, int pos, tdado dado);
// tdado removeLista(Lista lst, int pos);
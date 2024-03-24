#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct Node {
    char plate[20];
    struct Node* next;
} Node;

Node* createNode(char plate[]) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    strcpy(newNode->plate, plate);
    newNode->next = NULL;
    return newNode;
}

int calculateDebt(Node* semaphoreList, Node* speedList, Node* parkingList, char plate[]){
    int totalDebt = 0;

    Node* current = semaphoreList;
    while (current != NULL){
        if (strcmp(current->plate, plate) == 0){
            totalDebt += 300;
            break;
        }
        current = current->next;
    }

    current = speedList;
    while (current != NULL){
        if (strcmp(current->plate, plate) == 0){
            totalDebt += 200;
            break;
        }
        current = current->next;
    }

    current = parkingList;
    while (current != NULL){
        if (strcmp(current->plate, plate) == 0){
            totalDebt += 100;
            break;
        }
        current = current->next;
    }

    return totalDebt;
}

void findPlatesToRemove(Node* semaphoreList, Node* speedList, Node* parkingList){
    Node* current;

    current = semaphoreList;
    while (current != NULL){
        printf("Plate %s: Plate removal is required\n", current->plate);
        current = current->next;
    }

    current = speedList; 
    while (current != NULL){
        printf("Plate %s: Plate removal is required\n", current->plate);
        current = current->next;
    }

    current = parkingList;
    while (current != NULL){
        printf("Plate %s: Plate removal is required\n", current->plate);
        current = current->next;
    }
}

int main() {
    Node* semaphoreList = createNode("ABC1111");
    semaphoreList->next = createNode("XYZ9999");

    Node* speedList = createNode("ABC1111");
    speedList->next = createNode("NOP2222");

    Node* parkingList = createNode("XYZ9999");
    parkingList->next = createNode("KLM0000");

    char plate[] = "ABC1111";
    int debt = calculateDebt(semaphoreList, speedList, parkingList, plate);
    printf("Total debt for plate %s: %d Euro\n", plate, debt);

    printf("\nPlates for which removal is required:\n");
    findPlatesToRemove(semaphoreList, speedList, parkingList);

    return 0;
}

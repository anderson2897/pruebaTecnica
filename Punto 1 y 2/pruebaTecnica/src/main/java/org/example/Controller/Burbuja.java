package org.example.Controller;
import java.util.Random;

public class Burbuja {
    public static int[] ordenamiento(){
        Random random = new Random();
        int[] arreglo = new int[10];
        int tamanioArreglo = arreglo.length;

        for (int i = 0; i < tamanioArreglo - 1; i++) {
            arreglo[i] = random.nextInt(101);
        }
        for (int i = 0; i < tamanioArreglo - 1; i++) {
            for (int j = 0; j < tamanioArreglo - i - 1; j++) {
                if (arreglo[j] > arreglo[j + 1]) {
                    // Intercambiar arreglo[j] y arreglo[j+1]
                    int temp = arreglo[j];
                    arreglo[j] = arreglo[j + 1];
                    arreglo[j + 1] = temp;
                }
            }
        }

        for (int i = 0; i < tamanioArreglo; ++i) {
            System.out.print(arreglo[i] + " ");
        }

        return arreglo;
    }//ordenamiento

    public static void printArray(int[] arr) {
        int[] arreglo = new int[10];
        int tamanioArreglo = arreglo.length;

        System.out.println();
    }
}

package org.example;

import org.example.Controller.Burbuja;
import org.example.Controller.Fizzbuzz;
import java.util.Arrays;


// Press Shift twice to open the Search Everywhere dialog and type `show whitespaces`,
// then press Enter. You can now see whitespace characters in your code.
public class Main {
    public static void main(String[] args) {
        System.out.println("_____________FizzBuzz_____________");
        Fizzbuzz fizzbuzz = new Fizzbuzz();
        fizzbuzz.fizzbuzz();
        System.out.println("\n");

        System.out.println("_____________Burbuja_____________");
        Burbuja burbuja = new Burbuja();
        int[] arregloOrdenado = burbuja.ordenamiento();
    }//main
}//Main
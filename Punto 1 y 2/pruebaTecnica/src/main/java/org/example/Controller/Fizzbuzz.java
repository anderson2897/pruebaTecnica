package org.example.Controller;
import java.util.Random;

public class Fizzbuzz {
    Random random = new Random();
    public void fizzbuzz(){
        int numero;
        for (int i =0; i<11; i++){
            numero = random.nextInt(101);
            if (numero % 3 == 0 && numero % 5 == 0){
                System.out.println(numero + " " + "FizzBuzz");
            } else if (numero % 3 == 0) {
                System.out.println(numero + " " + "Fizz");
            }else if (numero % 5 == 0) {
                System.out.println(numero + " " + "Buzz");
            }else {
                System.out.println(numero + " " + "N");
            }
        }//for

    }//fizzbuzz

}//Fizzbuzz

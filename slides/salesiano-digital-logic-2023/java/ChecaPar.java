

public class ChecaPar { 

  public static void main(String[] args) { 

    int numeros[] = {0, 1, 2, 3, 4, 5}; 

    for (int numero : numeros) {
      System.out.println(ePar(numero)); 
    }
  }

  public static String ePar(int numero) {
      return ( numero % 2 == 0 )
        ? numero + " é par."
        : numero + " não é par.";
  }

}

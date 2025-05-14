import java.io.EOFException;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        
        Gestore g = new Gestore();
        Scanner scanner = new Scanner(System.in);
        g.dizionario.put(new Piattaforma("Google"), new Password("FilippoGoogle123."));
        
        //System.out.println(g.gare);

        try {
            FileOutputStream f = new FileOutputStream("password.dat",true);
            ObjectOutputStream fOUT = new ObjectOutputStream(f);
            fOUT.writeObject(g.dizionario);
            fOUT.flush();
            f.close();
        } catch (Exception e) {
            
        }
        
        try {
            FileInputStream f = new FileInputStream("gare.dat");
            ObjectInputStream fIN = new ObjectInputStream(f);
            while (true) {
                try {
                    System.out.println(fIN.readObject() );
                    
                } catch (EOFException e) {
                    break;
                }
            }
            f.close();
        } catch (Exception e) {
            // TODO: handle exception
        }
        
        
        System.out.println("\n\nInserisci piattaforma: ");
        String piattaforma_richiesta = scanner.nextLine();
        for(Piattaforma piattaforma : g.dizionario.keySet()){
            if(piattaforma.getPiattaforma().equals(piattaforma_richiesta)){
                System.out.println(g.dizionario.get(piattaforma));
            }
        }


    }
}

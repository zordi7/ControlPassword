import java.io.Serializable;

class Piattaforma implements Serializable{
       
    String piattaforma;

    Piattaforma(String piattaforma){
        this.piattaforma = piattaforma;
    }
    
    public String getPiattaforma() {
        return piattaforma;
    }
    
    @Override
    public String toString() {
    
        return piattaforma;
    }
        
}
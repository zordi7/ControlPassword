
import java.io.*;
class Password implements Serializable{
    String password;
    
    Password(String password){
        this.password = password;
    
    }
    public String getPassword() {
        return password;
    }
    @Override
    public String toString(){
        return password;
    }
}
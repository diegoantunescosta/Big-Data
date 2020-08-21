/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package aulavintecinco.view;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import com.mysql.jdbc.PreparedStatement;
import com.mysql.jdbc.Statement;
import javax.swing.JOptionPane;
/**
 *
 * @author diego
 */
public class Conexao {
Connection con;
    Statement stmt;
ResultSet rs;
  PreparedStatement ps;

    String url = "jdbc:mysql://localhost:3306/bancoaula";
    String user = "root";
    String password = "";
    String driver = "com.mysql.jdbc.Driver";
   
    public void OpenConexao()
    {
        try{
            Class.forName(driver).newInstance();
            con = DriverManager.getConnection(url, user, password);
            stmt = (Statement) con.createStatement();
    
        }catch(Exception e)
        {
            JOptionPane.showMessageDialog(null, "Erro na conexão com o BD ","ERRO",JOptionPane.ERROR_MESSAGE,null);
        }
    }
}
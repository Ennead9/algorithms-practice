import java.math.BigInteger;

public class QuadSieve {

    BigInteger n = BigInteger.valueOf(315);

    BigInteger g(BigInteger x, BigInteger n){
        return x.multiply(x).subtract(BigInteger.ONE).mod(n);
    }

    public static void main(String[] args) {
        
        QuadSieve gfg = new QuadSieve();

        BigInteger n = BigInteger.valueOf(315);
        BigInteger x = BigInteger.valueOf(2);
        BigInteger y = BigInteger.valueOf(2);
        BigInteger d = BigInteger.ONE;

        while(d.equals(BigInteger.ONE)){
            
            // Tortoise
            x = gfg.g(x, n);

            // Hare move
            y = gfg.g(gfg.g(y, n), n);

            // Check gcd of |x-y| and n
            d = x.subtract(y).abs().gcd(n);
        }

        if(d.equals(n)) {
            System.out.println("GCD not found for this");
        } else {
            System.out.println("One factor of "+n+ " is "+d);
        }

    }
}

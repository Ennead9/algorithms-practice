public class QuadSieve {

    int n = 315;
    public int gcd(int a, int b){
        int gcd = 0;
        for(int i = 1; i <= a || i <= b; i++){
            if(a % i == 0 && b % i == 0){
                gcd = i;
            }
        }
        return gcd;
    }

    int g(int x, int n) { return ((x * x) - 1) % n;}

    public static void main(String[] args) {
        
        QuadSieve gfg = new QuadSieve();

        int n = 315;
        int x = 2, y = 2, d = 1;

        while(d == 1){
            
            // Tortoise
            x = gfg.g(x, n);

            // Hare move
            y = gfg.g(gfg.g(y, n), n);

            // Check gcd of |x-y| and n
            d = gfg.gcd((x-y), gfg.n);
        }

        // fails to find prime factor
        if(d == gfg.n) {
            System.out.println("GCD not found for this");
        } else {
            System.out.println("One factor of "+n+ " is "+d);
        }

    }
}

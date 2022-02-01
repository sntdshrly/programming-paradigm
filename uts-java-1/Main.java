public class Main {
    public static void main(String[] args){
        Car test = new Car();
        test.setWheels(0);
        System.out.print("Harga mobil \"test\": ");
        System.out.println(test.getPrice());

        Car test2 = new Car();
        test2.setWheels(2);
        System.out.print("Harga mobil \"test2\": ");
        System.out.println(test2.getPrice());
    }
}

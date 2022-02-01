import java.util.Scanner;

public class Car extends Vehicle {
    private Wheel[] wheels;

    public void setWheels(int wheels){
        if (wheels == 0){
            wheels = 4;
            this.wheels = new Wheel[wheels];
            for (int i = 0; i < wheels; i++){
                this.wheels[i] = new Wheel(); //membuat objek wheel dengan default value
            }
            return;
        } else if(wheels < 3){
            Scanner sc = new Scanner(System.in);

            this.wheels = new Wheel[3];
            int index = 0;
            float harga = 0;
            float rata = 0;

            for (int i = 0; i < wheels; i++){  // Masukan price untuk jumlah wheel yang user input dahulu
                this.wheels[i] = new Wheel();
                System.out.print("Masukan harga wheel ke-" + String.valueOf(i + 1) + " : ");
                int t = Integer.parseInt(sc.next());
                this.wheels[i].setPrice(t);
                index++;
                harga += t;
            }
            sc.close();

            rata = harga / (index+1);
            // set harga tambahan
            int j = wheels;
            while (wheels < 3) {
                this.wheels[index] = new Wheel();
                harga += Math.round(rata);
                this.wheels[index].setPrice(Math.round(rata)); //bulatkan karena dibutuhkan int
                rata = harga / (index+1);
                wheels++;
            }
            
            System.out.println("\nAnda memasukan kurang dari 3 wheels, akan menambahkan " + String.valueOf(3 - j) + " wheels dengan harga rata\" dari wheels sebelumnya.");
        }
    }

    public int getPrice(){
        int sum = 0;
        for (Wheel wheel : wheels) {
            sum += wheel.getPrice();
        }

        return super.getBasePrice() + sum;
    }
}

public class Wheel {
    private int price;

    public Wheel(){
        this.setPrice(); //set price ke default value
    }

    public int getPrice(){
        return this.price;
    }

    public void setPrice(int price){
        if (price < 0){
            this.price = price * -1;
        } else {
            this.price = price;
        }
    }

    // method overload
    public void setPrice() {
        this.price = 1000;
    }
}

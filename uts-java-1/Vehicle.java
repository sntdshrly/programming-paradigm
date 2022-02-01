public class Vehicle{
    private int basePrice;

    public Vehicle(){
        this.setBasePrice(); //set base price ke default value;
    }
    
    public int getBasePrice(){
        return this.basePrice;
    }

    public void setBasePrice(int price){
        if (price < 0) {
            this.basePrice = price * -1;
        } else {
            this.basePrice = price;
        }
    }

    //overload method setBasePrice untuk default value 10000
    public void setBasePrice(){
        this.basePrice = 10000;
    }
}

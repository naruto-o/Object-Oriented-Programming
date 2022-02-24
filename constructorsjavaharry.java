package com.company;
//class CWH{
//    CWH(){
//        System.out.println("this is the default constructor");
//    }
//}
//class CWH{
//    CWH(String s, int b){
//        System.out.println("this is the " + b +"the video of " + " " + s);
//    }
//}
class MyEmployee{
    //first constructor
    MyEmployee(String s,int i){
        System.out.println("the name of the first employee is :" +s);
        System.out.println("the id of the first employee is" +i);
    }
//constructor overloaded
    MyEmployee(String s,int i ,int salary){
        System.out.println("the name of the second employee is :"+s);
        System.out.println("the id of the second employee is:"+i);
        System.out.println("the salary of second employeee is:"+salary);
    }
}

public class constructorsjavaharry {
//    Default constructor : A constructor with 0 parameters is known as default constructor.
//Paramerterized constructor : A constructor with some specified number of parameters is known
// as a parameterized constructor.

    public static void main(String[] args) {
//        CWH obj1 = new CWH();
//        CWH obj1 = new CWH("code with harry java playlist",42);
        MyEmployee shikhar = new MyEmployee("shikhar",1);
        MyEmployee saket = new MyEmployee("saket",5);

    }

}


            // SOURCE CODE OF VIDEO


//class MyMainEmployee{
//    private int id;
//    private String name;
//
//    public MyMainEmployee(){
//        id = 0;
//        name = "Your-Name-Here";
//    }
//    public MyMainEmployee(String myName, int myId){
//        id = myId;
//        name = myName;
//    }
//    public MyMainEmployee(String myName){
//        id = 1;
//        name = myName;
//    }
//    public String getName(){
//        return name;
//    }
//    public void setName(String n){
//        this.name = n;
//    }
//    public void setId(int i){
//        this.id = i;
//    }
//    public int getId(){
//        return id;
//    }
//}
//
//public class cwh_42_constructors {
//    public static void main(String[] args) {
//        //MyMainEmployee harry = new MyMainEmployee("ProgrammingWithHarry", 12);
//        MyMainEmployee harry = new MyMainEmployee();
//        //harry.setName("CodeWithHarry");
//        //harry.setId(34);
//        System.out.println(harry.getId());
//        System.out.println(harry.getName());
//    }
//}

import java.util.*;
public class oops {
	int empid;
	String ename,desg,company,address;
	float salary;
	Scanner sc=new Scanner(System.in);
	public void getEmployee(){
		empid=sc.nextInt();
		sc.nextLine();
		ename=sc.nextLine();
		desg=sc.nextLine();
		company=sc.nextLine();
		address=sc.nextLine();
		salary=sc.nextFloat();
		
	}
	public void displayEmployee(){
		System.out.println(empid+" "+ename+" "+desg+" "+company+" "+address+" "+salary);
	}
	public static void main(String[] args){
		// TODO Auto-generated method stub
		oops e1=new oops();
		e1.getEmployee();
		e1.displayEmployee();
	}

}

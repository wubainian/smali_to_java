package android.support.v4.app

import android.os.Parcelable;
import android.os.Parcelable$Creator;
import android.os.Bundle;
import android.os.Parcel;

final class FragmentState implements Parcelable{
	//instance field
	final String a;
	final int b;
	final boolean c;
	final int d;
	final int e;
	final String f;
	final boolean g;
	final boolean h;
	final Bundle i;
	Bundle j;
	android.support.v4.app.Fragment k;

	//static field
	public static final Parcelable$Creator CREATOR;

	//clinit method
	static{
	}

	//init method
	public FragmentState(Parcel aParcel0){
	}
	public FragmentState(android.support.v4.app.Fragment aFragment0){
	}

	//ordinary method
	public android.support.v4.app.Fragment a(android.support.v4.app.FragmentActivity aFragmentActivity0, android.support.v4.app.Fragment aFragment0){
	}
	public int describeContents(){
	}
	public void writeToParcel(Parcel aParcel0, int aint0){
	}

}


package com.google.android.gms.analytics.internal

import android.os.Parcelable;
import android.os.Parcelable$Creator;
import android.os.Parcel;

public class Command implements Parcelable{
	//instance field
	private String a;
	private String b;
	private String c;

	//static field
	public static final Parcelable$Creator CREATOR;

	//clinit method
	static{
	}

	//init method
	public Command(){
	}
	Command(Parcel aParcel0){
	}

	//ordinary method
	private void a(Parcel aParcel0){
	}
	public int describeContents(){
	}
	public void writeToParcel(Parcel aParcel0, int aint0){
	}

}


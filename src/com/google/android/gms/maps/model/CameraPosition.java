package com.google.android.gms.maps.model

import android.content.Context;
import android.os.Parcel;

public final class CameraPosition implements com.google.android.gms.common.internal.safeparcel.SafeParcelable{
	//instance field
	public final com.google.android.gms.maps.model.LatLng a;
	public final float b;
	public final float c;
	public final float d;
	private final int e;

	//static field
	public static final com.google.android.gms.maps.model.c CREATOR;

	//clinit method
	static{
	}

	//init method
	CameraPosition(int aint0, com.google.android.gms.maps.model.LatLng aLatLng0, float afloat0, float afloat0, float afloat0){
	}
	public CameraPosition(com.google.android.gms.maps.model.LatLng aLatLng0, float afloat0, float afloat0, float afloat0){
	}

	//ordinary method
	public static com.google.android.gms.maps.model.CameraPosition a(Context aContext0, android.util.AttributeSet aAttributeSet0){
	}
	public static com.google.android.gms.maps.model.b b(){
	}
	int a(){
	}
	public int describeContents(){
	}
	public boolean equals(Object aObject0){
	}
	public int hashCode(){
	}
	public String toString(){
	}
	public void writeToParcel(Parcel aParcel0, int aint0){
	}

}


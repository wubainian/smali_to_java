package com.google.android.gms.games.multiplayer

import android.os.Parcelable;

public interface abstract class Invitation implements Parcelable, com.google.android.gms.common.data.a, com.google.android.gms.games.multiplayer.e,{
	//ordinary method
	public abstract com.google.android.gms.games.Game b();
	public abstract String c();
	public abstract com.google.android.gms.games.multiplayer.Participant d();
	public abstract long e();
	public abstract int f();
	public abstract int g();

}


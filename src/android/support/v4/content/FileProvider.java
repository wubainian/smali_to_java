package android.support.v4.content

import android.content.ContentProvider;
import java.io.File;
import java.util.HashMap;
import android.content.Context;
import android.content.pm.ProviderInfo;
import android.content.ContentValues;
import android.os.ParcelFileDescriptor;

public class FileProvider extends ContentProvider{
	//instance field
	private android.support.v4.content.a d;

	//static field
	private static final []java.lang.String a;
	private static final File b;
	private static HashMap c;

	//clinit method
	static{
	}

	//init method
	public FileProvider(){
	}

	//ordinary method
	private static int a(String aString0){
	}
	private static android.support.v4.content.a a(Context aContext0, String aString0){
	}
	private static varargs File a(File aFile0, []java.lang.String aString0){
	}
	private static []java.lang.Object a([]java.lang.Object aObject0, int aint0){
	}
	private static []java.lang.String a([]java.lang.String aString0, int aint0){
	}
	private static android.support.v4.content.a b(Context aContext0, String aString0){
	}
	public void attachInfo(Context aContext0, ProviderInfo aProviderInfo0){
	}
	public int delete(android.net.Uri aUri0, String aString0, []java.lang.String aString0){
	}
	public String getType(android.net.Uri aUri0){
	}
	public android.net.Uri insert(android.net.Uri aUri0, ContentValues aContentValues0){
	}
	public boolean onCreate(){
	}
	public ParcelFileDescriptor openFile(android.net.Uri aUri0, String aString0){
	}
	public android.database.Cursor query(android.net.Uri aUri0, []java.lang.String aString0, String aString0, []java.lang.String aString0, String aString0){
	}
	public int update(android.net.Uri aUri0, ContentValues aContentValues0, String aString0, []java.lang.String aString0){
	}

}


package android.support.v4.app

import android.app.Activity;
import android.os.Handler;
import android.view.View;
import java.io.PrintWriter;
import android.view.Menu;
import java.io.FileDescriptor;
import android.content.Intent;
import android.content.res.Configuration;
import android.os.Bundle;
import android.content.Context;
import android.view.KeyEvent;
import android.view.MenuItem;

public class FragmentActivity extends Activity{
	//instance field
	final Handler a;
	final android.support.v4.app.o b;
	final android.support.v4.app.l c;
	boolean d;
	boolean e;
	boolean f;
	boolean g;
	boolean h;
	boolean i;
	boolean j;
	boolean k;
	android.support.v4.b.l l;
	android.support.v4.app.z m;

	//init method
	public FragmentActivity(){
	}

	//ordinary method
	private static String a(View aView0){
	}
	private void a(String aString0, PrintWriter aPrintWriter0, View aView0){
	}
	android.support.v4.app.z a(String aString0, boolean aboolean0, boolean aboolean0){
	}
	protected void a(){
	}
	public void a(android.support.v4.app.Fragment aFragment0){
	}
	void a(String aString0){
	}
	void a(boolean aboolean0){
	}
	protected boolean a(View aView0, Menu aMenu0){
	}
	public Object b(){
	}
	public void c(){
	}
	void d(){
	}
	public void dump(String aString0, FileDescriptor aFileDescriptor0, PrintWriter aPrintWriter0, []java.lang.String aString0){
	}
	protected void onActivityResult(int aint0, int aint0, Intent aIntent0){
	}
	public void onBackPressed(){
	}
	public void onConfigurationChanged(Configuration aConfiguration0){
	}
	protected void onCreate(Bundle aBundle0){
	}
	public boolean onCreatePanelMenu(int aint0, Menu aMenu0){
	}
	public View onCreateView(String aString0, Context aContext0, android.util.AttributeSet aAttributeSet0){
	}
	protected void onDestroy(){
	}
	public boolean onKeyDown(int aint0, KeyEvent aKeyEvent0){
	}
	public void onLowMemory(){
	}
	public boolean onMenuItemSelected(int aint0, MenuItem aMenuItem0){
	}
	protected void onNewIntent(Intent aIntent0){
	}
	public void onPanelClosed(int aint0, Menu aMenu0){
	}
	protected void onPause(){
	}
	protected void onPostResume(){
	}
	public boolean onPreparePanel(int aint0, View aView0, Menu aMenu0){
	}
	protected void onResume(){
	}
	public final Object onRetainNonConfigurationInstance(){
	}
	protected void onSaveInstanceState(Bundle aBundle0){
	}
	protected void onStart(){
	}
	protected void onStop(){
	}
	public void startActivityForResult(Intent aIntent0, int aint0){
	}

}


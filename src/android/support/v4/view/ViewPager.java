package android.support.v4.view

import android.view.ViewGroup;
import java.util.Comparator;
import android.view.animation.Interpolator;
import android.view.VelocityTracker;
import java.util.ArrayList;
import android.os.Parcelable;
import android.content.Context;
import android.view.View;
import android.view.MotionEvent;
import android.view.KeyEvent;
import android.view.ViewGroup$LayoutParams;
import android.view.accessibility.AccessibilityEvent;

public class ViewPager extends ViewGroup{
	//instance field
	private boolean A;
	private boolean B;
	private int C;
	private int D;
	private int E;
	private float F;
	private float G;
	private float H;
	private float I;
	private int J;
	private VelocityTracker K;
	private int L;
	private int M;
	private int N;
	private int O;
	private boolean P;
	private android.support.v4.widget.h Q;
	private android.support.v4.widget.h R;
	private boolean S;
	private boolean T;
	private boolean U;
	private int V;
	private android.support.v4.view.cc W;
	private android.support.v4.view.cc Z;
	private android.support.v4.view.cb aa;
	private android.support.v4.view.cd ab;
	private Method ac;
	private int ad;
	private ArrayList ae;
	private final Runnable ag;
	private int ah;
	private int b;
	private final ArrayList e;
	private final android.support.v4.view.bz f;
	private final android.graphics.Rect g;
	private android.support.v4.view.ae h;
	private int i;
	private int j;
	private Parcelable k;
	private ClassLoader l;
	private android.widget.Scroller m;
	private android.support.v4.view.ce n;
	private int o;
	private android.graphics.drawable.Drawable p;
	private int q;
	private int r;
	private float s;
	private float t;
	private int u;
	private int v;
	private boolean w;
	private boolean x;
	private boolean y;
	private int z;

	//static field
	private static final []int a;
	private static final android.support.v4.view.cg af;
	private static final Comparator c;
	private static final Interpolator d;

	//clinit method
	static{
	}

	//init method
	public ViewPager(Context aContext0, android.util.AttributeSet aAttributeSet0){
	}

	//ordinary method
	private int a(int aint0, float afloat0, int aint0, int aint0){
	}
	private android.graphics.Rect a(android.graphics.Rect aRect0, View aView0){
	}
	static synthetic android.support.v4.view.ae a(android.support.v4.view.ViewPager aViewPager0){
	}
	private void a(int aint0, int aint0, int aint0, int aint0){
	}
	private void a(int aint0, boolean aboolean0, int aint0, boolean aboolean0){
	}
	static synthetic void a(android.support.v4.view.ViewPager aViewPager0, int aint0){
	}
	private void a(android.support.v4.view.bz abz0, int aint0, android.support.v4.view.bz abz0){
	}
	private void a(MotionEvent aMotionEvent0){
	}
	private void a(boolean aboolean0){
	}
	private boolean a(float afloat0, float afloat0){
	}
	static synthetic int b(android.support.v4.view.ViewPager aViewPager0){
	}
	private void b(boolean aboolean0){
	}
	private boolean b(float afloat0){
	}
	private void c(boolean aboolean0){
	}
	private boolean d(int aint0){
	}
	static synthetic []int f(){
	}
	private void g(){
	}
	private int getClientWidth(){
	}
	private void h(){
	}
	private android.support.v4.view.bz i(){
	}
	private void j(){
	}
	private void setScrollState(int aint0){
	}
	private void setScrollingCacheEnabled(boolean aboolean0){
	}
	float a(float afloat0){
	}
	android.support.v4.view.bz a(int aint0, int aint0){
	}
	android.support.v4.view.bz a(View aView0){
	}
	android.support.v4.view.cc a(android.support.v4.view.cc acc0){
	}
	void a(){
	}
	void a(int aint0){
	}
	protected void a(int aint0, float afloat0, int aint0){
	}
	void a(int aint0, int aint0, int aint0){
	}
	public void a(int aint0, boolean aboolean0){
	}
	void a(int aint0, boolean aboolean0, boolean aboolean0){
	}
	void a(int aint0, boolean aboolean0, boolean aboolean0, int aint0){
	}
	public boolean a(KeyEvent aKeyEvent0){
	}
	protected boolean a(View aView0, boolean aboolean0, int aint0, int aint0, int aint0){
	}
	public void addFocusables(ArrayList aArrayList0, int aint0, int aint0){
	}
	public void addTouchables(ArrayList aArrayList0){
	}
	public void addView(View aView0, int aint0, ViewGroup$LayoutParams aViewGroup$LayoutParams0){
	}
	android.support.v4.view.bz b(int aint0){
	}
	android.support.v4.view.bz b(View aView0){
	}
	void b(){
	}
	void c(){
	}
	public boolean c(int aint0){
	}
	public boolean canScrollHorizontally(int aint0){
	}
	protected boolean checkLayoutParams(ViewGroup$LayoutParams aViewGroup$LayoutParams0){
	}
	public void computeScroll(){
	}
	boolean d(){
	}
	public boolean dispatchKeyEvent(KeyEvent aKeyEvent0){
	}
	public boolean dispatchPopulateAccessibilityEvent(AccessibilityEvent aAccessibilityEvent0){
	}
	public void draw(android.graphics.Canvas aCanvas0){
	}
	protected void drawableStateChanged(){
	}
	boolean e(){
	}
	protected ViewGroup$LayoutParams generateDefaultLayoutParams(){
	}
	public ViewGroup$LayoutParams generateLayoutParams(android.util.AttributeSet aAttributeSet0){
	}
	protected ViewGroup$LayoutParams generateLayoutParams(ViewGroup$LayoutParams aViewGroup$LayoutParams0){
	}
	public android.support.v4.view.ae getAdapter(){
	}
	protected int getChildDrawingOrder(int aint0, int aint0){
	}
	public int getCurrentItem(){
	}
	public int getOffscreenPageLimit(){
	}
	public int getPageMargin(){
	}
	protected void onAttachedToWindow(){
	}
	protected void onDetachedFromWindow(){
	}
	protected void onDraw(android.graphics.Canvas aCanvas0){
	}
	public boolean onInterceptTouchEvent(MotionEvent aMotionEvent0){
	}
	protected void onLayout(boolean aboolean0, int aint0, int aint0, int aint0, int aint0){
	}
	protected void onMeasure(int aint0, int aint0){
	}
	protected boolean onRequestFocusInDescendants(int aint0, android.graphics.Rect aRect0){
	}
	public void onRestoreInstanceState(Parcelable aParcelable0){
	}
	public Parcelable onSaveInstanceState(){
	}
	protected void onSizeChanged(int aint0, int aint0, int aint0, int aint0){
	}
	public boolean onTouchEvent(MotionEvent aMotionEvent0){
	}
	public void removeView(View aView0){
	}
	public void setAdapter(android.support.v4.view.ae aae0){
	}
	void setChildrenDrawingOrderEnabledCompat(boolean aboolean0){
	}
	public void setCurrentItem(int aint0){
	}
	public void setOffscreenPageLimit(int aint0){
	}
	void setOnAdapterChangeListener(android.support.v4.view.cb acb0){
	}
	public void setOnPageChangeListener(android.support.v4.view.cc acc0){
	}
	public void setPageMargin(int aint0){
	}
	public void setPageMarginDrawable(int aint0){
	}
	public void setPageMarginDrawable(android.graphics.drawable.Drawable aDrawable0){
	}
	protected boolean verifyDrawable(android.graphics.drawable.Drawable aDrawable0){
	}

}


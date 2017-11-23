package com.yhxu.contactstest;

import android.content.Context;
import android.graphics.Canvas;
import android.graphics.Color;
import android.graphics.Paint;
import android.graphics.RectF;
import android.util.AttributeSet;
import android.view.View;

public class RectFView extends View{

	private Paint paint;
	private RectF rectF;

	public RectFView(Context context, AttributeSet attrs) {
		super(context, attrs);
		init();
	}
	
	private void init(){
		paint = new Paint();
		paint.setColor(Color.RED);
		rectF = new RectF();
		rectF.set(100, 100, 600, 600);
	}
	
	// 恢复到初始状态
	public void recover(){
		rectF.set(100,100,600,600);
		invalidate();
	}
	
	/**
	 *  dx 和 dy 通过 EditText 输入参数来动态改变 
	 */
	public void inset(float dx, float dy){
		rectF.inset(dx, dy);
		invalidate();
	}
	
	
	@Override
	protected void onDraw(Canvas canvas) {
		super.onDraw(canvas);
		
		canvas.drawRect(rectF, paint);
		
	}
	

}

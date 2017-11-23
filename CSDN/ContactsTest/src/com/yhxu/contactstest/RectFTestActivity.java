package com.yhxu.contactstest;

import android.app.Activity;
import android.os.Bundle;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.EditText;

public class RectFTestActivity extends Activity{
	
	private RectFView rectFView;
	private EditText etDx;
	private EditText etDy;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_rectf_test);
		
		rectFView = (RectFView) findViewById(R.id.rectf_view);
		etDx = (EditText) findViewById(R.id.et_dx);
		etDy = (EditText) findViewById(R.id.et_dy);
		
		findViewById(R.id.btn_inset).setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				String stringDx = etDx.getText().toString();
				String stringDy = etDy.getText().toString();
				float dx ;
				float dy ;
				try{
					dx = Float.valueOf(stringDx);
				}catch(Exception e){
					dx = 0;
				}
				
				try{
					dy = Float.valueOf(stringDy);
				}catch(Exception e){
					dy = 0;
				}
				rectFView.inset(dx, dy);
			}
		});
		
		findViewById(R.id.btn_recover).setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				rectFView.recover();
			}
		});
		
	}
	

}

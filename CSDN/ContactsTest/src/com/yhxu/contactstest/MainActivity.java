package com.yhxu.contactstest;

import android.app.Activity;
import android.content.Intent;
import android.graphics.Bitmap;
import android.graphics.Matrix;
import android.graphics.Rect;
import android.graphics.RectF;
import android.graphics.drawable.Drawable;
import android.net.Uri;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.view.View.OnClickListener;
import android.widget.ArrayAdapter;
import android.widget.AutoCompleteTextView;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import com.yhxu.contact.ContactsActivity;

public class MainActivity extends Activity {
	private TextView contact_show;
	Bitmap bitmap = null;
    private float dis=0;
	private ImageView ivMatrix;

	@Override
	protected void onCreate(Bundle savedInstanceState) {
		super.onCreate(savedInstanceState);
		setContentView(R.layout.activity_main);
		contact_show = (TextView) findViewById(R.id.contact_show);
		Button contact_btn = (Button) findViewById(R.id.contact_btn);
		contact_btn.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				Intent intent = new Intent(MainActivity.this, ContactsActivity.class);
				startActivityForResult(intent, 2);
			}
		});
		
		Button btnEntryRectf = (Button) findViewById(R.id.btn_entry_rectf_activity);
		btnEntryRectf.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				Intent intent = new Intent(MainActivity.this, RectFTestActivity.class);
				startActivity(intent);
			}
		});
		
		
		AutoCompleteTextView et = (AutoCompleteTextView) findViewById(R.id.et_auto);
//		ArrayAdapter<String> adapter = new ArrayAdapter<String>(this, android.R.layout.simple_spinner_dropdown_item,)
//		et.setAdapter(adapter);
		
		ivMatrix = (ImageView) findViewById(R.id.iv_matrix_demo);
		ivMatrix.setOnClickListener(new OnClickListener() {
			
			@Override
			public void onClick(View v) {
				Matrix matrix = new Matrix();
				dis += 100f;
				matrix.setTranslate(dis, dis);
				matrix.postTranslate(10, 10);
				ivMatrix.setImageMatrix(matrix);
				
				Drawable drawable = ivMatrix.getDrawable();
				if( drawable != null ){
					Rect rect = drawable.getBounds();
					RectF rectf = new RectF();
					rectf.set(0, 0, drawable.getIntrinsicWidth(), drawable.getIntrinsicHeight());
					Log.e("tag","before : " + "left : " + rectf.left + "right : " + rectf.right
							+ " top : " + rectf.top + " bottom : "+ rectf.bottom);
					// 0 , 144 , 0 , 144
					matrix.mapRect(rectf);
					Log.e("tag","after : " + "left : " + rectf.left + "right : " + rectf.right
							+ " top : " + rectf.top + " bottom : "+ rectf.bottom);
					// 110 , 254 , 110 , 254
					// 210 , 354 , 210 , 354
					// 310 , 454 , 310 , 454
					
				}
			}
		});
	}
	
	/**
	 * ͨѶ¼���ά��ɨ��ص��¼�
	 */
	protected void onActivityResult(int requestCode, int resultCode, Intent data) {
		 if (requestCode == 2 && resultCode == 20) {// ͨѶ¼������
			 contact_show.setText("������"+data.getExtras().get("Name")+"\n���룺"+data.getExtras().get("phoneNumber"));
		 }
	}
}

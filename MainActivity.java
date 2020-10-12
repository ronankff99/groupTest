package com.example.myfirstform;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.text.TextUtils;
import android.util.Log;
import android.util.Patterns;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity {
    EditText firstName;
    EditText lastName;
    EditText address;
    EditText email;
    Button registerBtn;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        firstName = findViewById(R.id.firstName);
        lastName = findViewById(R.id.lastName);
        address = findViewById(R.id.postalAddress);
        email = findViewById(R.id.email);
        registerBtn = findViewById(R.id.registerBtn);

        registerBtn.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                checkDataEntered();
            }
        });
    }

    void checkDataEntered(){
        //if (isEmpty(firstName)||isEmpty(lastName)||isEmail(email)){
        if (isEmpty(firstName)||isEmpty(lastName)){
            Toast t = Toast.makeText(this, "Missing fields", Toast.LENGTH_SHORT);
            t.show();
        }
        else{
            try {
                JSONObject jsonObject = new JSONObject("{\"firstName\":\"" + firstName.getText().toString() + "\"," +
                        "\"lastName\":\""+ lastName.getText().toString() + "\"," +
                        "\"address\":\"" + address.getText().toString() + "\"," +
                        "\"email\":\"" + email.getText().toString() + "\"}");
                Toast t = Toast.makeText(this, "" + jsonObject.toString() + "", Toast.LENGTH_SHORT);
                t.show();
            }catch (JSONException err){
                Log.d("Error", err.toString());
            }
        }
    }

    boolean isEmail(EditText text){
        CharSequence email = text.getText().toString();
        return(TextUtils.isEmpty(email) || Patterns.EMAIL_ADDRESS.matcher(email).matches());
    }

    boolean isEmpty(EditText text){
        CharSequence str = text.getText().toString();
        return TextUtils.isEmpty(str);
    }
}


package com.example.housevalue;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.AdapterView;
import android.widget.ArrayAdapter;
import android.widget.Button;
import android.widget.CompoundButton;
import android.widget.EditText;
import android.widget.Spinner;
import android.widget.Switch;
import android.widget.Toast;

import org.json.JSONException;
import org.json.JSONObject;

public class MainActivity extends AppCompatActivity implements AdapterView.OnItemSelectedListener{

    Spinner spinner1;
    Spinner spinner2;
    EditText numberBedrooms;
    EditText numberBathrooms;
    EditText squareFootageLivingRoom;
    EditText squareFootageLot;
    EditText numberFloors;
    Switch waterfront;
    Switch scenic;
    Button check;
    Boolean waterfrontState;
    Boolean scenicState;
    String houseGradingString;
    String energyGradingString;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

                    //creating drop down list for house condition grading
        spinner1 = findViewById(R.id.spinner1);
        ArrayAdapter<CharSequence> adapter1 = ArrayAdapter.createFromResource(this,R.array.houseGrading, android.R.layout.simple_spinner_item);
        adapter1.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner1.setAdapter(adapter1);
        spinner1.setOnItemSelectedListener(this);

                    //creating drop down list for energy grading
        spinner2 = findViewById(R.id.spinner2);
        ArrayAdapter<CharSequence> adapter2 = ArrayAdapter.createFromResource(this, R.array.energyGrading, android.R.layout.simple_spinner_item);
        adapter2.setDropDownViewResource(android.R.layout.simple_spinner_dropdown_item);
        spinner2.setAdapter(adapter2);
        spinner2.setOnItemSelectedListener(this);

        numberBedrooms = findViewById(R.id.numberBedrooms);
        numberBathrooms = findViewById(R.id.numberBathrooms);
        squareFootageLivingRoom = findViewById(R.id.squareFootageLivingRoom);
        squareFootageLot = findViewById(R.id.squareFootageLot);
        numberFloors = findViewById(R.id.numberFloors);

        waterfront = findViewById(R.id.waterfront);
        scenic = findViewById(R.id.scenic);

        check = findViewById(R.id.check);

        waterfrontState = false;
        scenicState = false;
        waterfront.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked == true){
                    waterfrontState = true;
                }
            }
        });

        scenic.setOnCheckedChangeListener(new CompoundButton.OnCheckedChangeListener() {
            @Override
            public void onCheckedChanged(CompoundButton buttonView, boolean isChecked) {
                if(isChecked == true){
                    scenicState = true;
                }
            }
        });

        check.setOnClickListener(new View.OnClickListener(){
            @Override
            public void onClick(View view){
                checkDataEntered();
            }
        });

    }

    @Override
    public void onItemSelected(AdapterView<?> parent, View view, int position, long id) {
        String text = parent.getItemAtPosition(position).toString();
        if(parent.getId() == R.id.spinner1){
            houseGradingString = text;
        }
        else if(parent.getId() == R.id.spinner2){
            energyGradingString = text;
        }
    }

    @Override
    public void onNothingSelected(AdapterView<?> parent) {

    }

    public void checkDataEntered(){
        try {
            JSONObject jsonObject = new JSONObject("{" +
                    "\"numberBedrooms\":" + numberBedrooms.getText() + "," +
                    "\"numberBathrooms\":"+ numberBathrooms.getText() + "," +
                    "\"squareFootageLivingRoom\":" + squareFootageLivingRoom.getText() + "," +
                    "\"squareFootageLot\":" + squareFootageLot.getText() + "," +
                    "\"numberFloors\":" + numberFloors.getText() + "," +
                    "\"waterfront\":" + waterfrontState + "," +
                    "\"scenic\":" + scenicState + "," +
                    "\"houseGrading\":" + houseGradingString + "," +
                    "\"energyGrading\":" + energyGradingString + "}");
            Toast.makeText(this, "" + jsonObject.toString() + "", Toast.LENGTH_SHORT).show();
            System.out.println(jsonObject);
        } catch (JSONException e) {
            e.printStackTrace();
        }
    }
}
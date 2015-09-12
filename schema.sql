CREATE TABLE physicians (
    id SERIAL PRIMARY KEY,
    firstname VARCHAR,
    lastname VARCHAR,
    specialty INT REFERENCES specialty(id),
);

CREATE TABLE specialty (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
);

CREATE TABLE appointments (
    id SERIAL PRIMARY KEY,
    patientname VARCHAR
    appointmenttime TIMESTAMP WITH TIME ZONE
    procedure VARCHAR #change to ICD-10
);

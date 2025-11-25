import unittest
import pandas as pd
import os
import streamlit as st
from app import cargar_datos_maestros, cargar_seguimiento, guardar_seguimiento
from calendario_module import cargar_calendario, guardar_registro

class TestAppLogic(unittest.TestCase):

    def setUp(self):
        # Define file paths
        self.archivo_datos = "LISTADO-CON-FASES.csv"
        self.archivo_seguimiento = "seguimiento_informes.csv"
        self.archivo_calendario = "calendario.csv"

        # Create dummy CSV for LISTADO-CON-FASES.csv with a dummy first line
        centros_df = pd.DataFrame({
            'NOMBRE DEL CENTRO': ['Centro A', 'Centro B'],
            'PROVINCIA': ['Provincia A', 'Provincia B'],
            'CANTON': ['Canton A', 'Canton B'],
            'CODIGO PRESUPUESTARIO': ['001', '002'],
            'CATALOGO': ['1', '2']
        })
        with open(self.archivo_datos, 'w') as f:
            f.write("Dummy header line to be skipped\n")
            centros_df.to_csv(f, index=False)

        # Create dummy CSV for seguimiento_informes.csv
        seguimiento_df = pd.DataFrame({
            'ID': [1, 2],
            'Centro': ['Centro A', 'Centro B'],
            'Estado': ['Pendiente', 'En Proceso'],
            'Fecha_Inicio': ['2023-01-01', '2023-01-02'],
            'Fecha_Fin': [None, None],
            'Responsable': ['John Doe', 'Jane Doe'],
            'Prioridad': ['Alta', 'Media']
        })
        seguimiento_df.to_csv(self.archivo_seguimiento, index=False)

        # Create dummy CSV for calendario.csv
        calendario_df = pd.DataFrame({
            'ID_Cita': [1],
            'Fecha': ['2023-01-01'],
            'Hora': [9],
            'Centro': ['Centro A'],
            'Estado': ['Pendiente']
        })
        calendario_df.to_csv(self.archivo_calendario, index=False)

    def tearDown(self):
        # Clean up dummy files
        for f in [self.archivo_datos, self.archivo_seguimiento, self.archivo_calendario]:
            if os.path.exists(f):
                os.remove(f)
        st.cache_data.clear()

    def test_cargar_datos_maestros(self):
        """Test that the master data is loaded and columns are normalized correctly."""
        st.cache_data.clear()
        df = cargar_datos_maestros()
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 2, "Should load 2 rows of data.")
        expected_cols = ["NOMBRE", "PROVINCIA", "CANTON", "CODIGO", "CATALOGO"]
        self.assertListEqual(sorted(list(df.columns)), sorted(expected_cols), "Columns should be correctly mapped and normalized.")

    def test_cargar_seguimiento(self):
        """Test loading the tracking data."""
        df = cargar_seguimiento()
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 2)

    def test_guardar_seguimiento(self):
        """Test saving changes to the tracking data."""
        df = cargar_seguimiento()
        self.assertEqual(df.loc[0, 'Estado'], 'Pendiente')
        df.loc[0, 'Estado'] = 'Terminado'
        guardar_seguimiento(df)
        df_updated = cargar_seguimiento()
        self.assertEqual(df_updated.loc[0, 'Estado'], 'Terminado')

    def test_cargar_calendario(self):
        """Test loading the calendar data."""
        df = cargar_calendario(self.archivo_calendario)
        self.assertIsNotNone(df)
        self.assertEqual(len(df), 1)

    def test_guardar_registro_calendario(self):
        """Test adding a new record to the calendar."""
        nuevo_registro = {
            'ID_Cita': 2, 'Fecha': '2023-01-02', 'Hora': 10,
            'Centro': 'Centro C', 'Estado': 'Confirmada'
        }

        guardar_registro(self.archivo_calendario, nuevo_registro)

        df_updated = cargar_calendario(self.archivo_calendario)
        self.assertEqual(len(df_updated), 2)
        self.assertEqual(df_updated.iloc[1]['Estado'], 'Confirmada')

if __name__ == '__main__':
    # Need to redefine the global constants from app.py for the tests to work
    import app
    app.ARCHIVO_DATOS = "LISTADO-CON-FASES.csv"
    app.ARCHIVO_SEGUIMIENTO = "seguimiento_informes.csv"
    app.ARCHIVO_CALENDARIO = "calendario.csv"

    unittest.main()

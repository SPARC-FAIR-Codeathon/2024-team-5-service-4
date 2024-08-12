import argparse

import vtk
from sparc.client.zinchelper import ZincHelper

def fetch_vtk_from_dataset(ID):
    # Create a ZincHelper instance
    zinc = ZincHelper()

    # Use the get_scaffold_as_vtk() function to export scaffold data to vtk format
    zinc.get_scaffold_as_vtk(ID)

    # Define the input and output paths
    input_vtk_file = "scaffold_root.vtk"
    output_1 = "scaffold.vtk"

    # Create a generic reader for the VTK file
    reader = vtk.vtkDataSetReader()
    reader.SetFileName(input_vtk_file)
    reader.Update()

    # Get the output of the reader
    data = reader.GetOutput()

    # Check the type of the output and choose the appropriate writer
    if isinstance(data, vtk.vtkPolyData):
        writer = vtk.vtkPolyDataWriter()
        writer.SetInputData(data)
    elif isinstance(data, vtk.vtkUnstructuredGrid):
        writer = vtk.vtkUnstructuredGridWriter()
        writer.SetInputData(data)
    else:
        raise TypeError("Unsupported VTK data type: " + type(data).__name__)

    # Set the output file name and write the data
    writer.SetFileName(output_1)
    writer.Write()
    print(f"VTK file for Dataset ID {ID} saved as: {output_1}")


# Example usage
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('id', help='Dataset ID')
    args = parser.parse_args()

    dataset_id = args.id
    print(f"Fetching VTK for Dataset ID: {dataset_id}")
    fetch_vtk_from_dataset(dataset_id)
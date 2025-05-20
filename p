/*--------------------------------*- C++ -*----------------------------------*\
| =========                 |                                                 |
| \\      /  F ield         | OpenFOAM: The Open Source CFD Toolbox           |
|  \\    /   O peration     | Version:  v2406                                 |
|   \\  /    A nd           | Website:  www.openfoam.com                      |
|    \\/     M anipulation  |                                                 |
\*---------------------------------------------------------------------------*/
FoamFile
{
    version     2.0;
    format      ascii;
    class       volScalarField;
    object      p;
}
// * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * //

dimensions      [0 2 -2 0 0 0 0];

internalField   uniform 0;

boundaryField
{
    rotatingAMI
    {
        type 			cyclicAMI;
    }

    fixedAMI
    {
        type		    cyclicAMI;
    }

    inlet
    {
        type zeroGradient;
	}

    outlet
    {
        type 			fixedValue;
        value           uniform 0;
    }

    blade1
    {
        type zeroGradient;
    }

    blade2
    {
        type zeroGradient;
    }

    blade3
    {
        type zeroGradient;
    }

    hub
    {
        type zeroGradient;
    }

	movingHub
	{
        type zeroGradient;
    }
	
	
	surroundingsNoSlip
    {
        type zeroGradient;
    }
	
	surroundingsSlip
    {
        type zeroGradient;
    }
}


// ************************************************************************* //

from pyscript import display, document


def identifying_temp(e):
    document.getElementById('output').innerHTML = "Diagnosis:"
    fahrenheit = float(document.getElementById('fahrenheit').value) # collecting value from an input field
    celcius = round((fahrenheit - 32) * 5/9, 2)

    if celcius > 37.7:
        display(f'You have a fever of {celcius}.', target='output')
    else:
        display(f'You have a normal temperature of {celcius}.', target='output')
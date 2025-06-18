def savings(gross_pay, tax_rate, expenses):
    print(gross_pay - (gross_pay * tax_rate) - expenses)

savings(1000, 0, 500)
500


def material_waste(total_material, material_units, num_jobs, job_consumption):
    value = total_material - (num_jobs * job_consumption)
    unit = material_units
    result = str(value) + unit
    print(result)

material_waste(1000,"kg",3,100)
700kg


def interest(principal, rate, periods):
    final_value = principal + (principal * (rate * periods))
    print(final_value)

interest(1000,0.06,8)
1480.0
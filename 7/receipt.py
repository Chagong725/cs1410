# imports module
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.styles import ParagraphStyle


def make_receipt(order, filename, total_cost, total_tax):
    data = [("Item", " ","Price", "Tax")]
    for item in order:
        item_data = [item.name, " ", "%.2f" % item.calculate_cost(), "%.2f" % item.calculate_tax()]
        data.append(item_data)
    data.append(["Order Price: ", "%.2f" % total_cost, 'Total Cost: ' , "%.2f" % total_tax])

    gridlength = len(data) - 2
    

    pdf = SimpleDocTemplate(filename, pagesize = A4)
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle("Title Style", 
                             parent=styles["Normal"], 
                             fontSize=20, 
                             alignment=1,
                             textColor=colors.black)
    title_style.alignment = 1
    title = Paragraph("Receipt", title_style)

    style = TableStyle(
	[
		( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
		( "GRID" , ( 0, 0 ), ( 4, gridlength ), 1 , colors.black ),
		( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.gray ),
		( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.whitesmoke ),
		( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
		( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.beige ),
	]
    )

    table = Table( data , style = style )
    pdf.build([title, Spacer(1, 20), table])

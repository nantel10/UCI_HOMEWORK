Sub stock_market()

Dim ticker As String

Dim tickertotal As Integer
tickertotal = 2

Dim openprice As Double

Dim nextopenprice As Double
nextopenprice = 2

Dim closeprice As Double

Dim yearlychange As Double

Dim percentchange As Double

Dim ticker_row As Integer
ticker_row = 2

Dim stockvolume as Double
stockvolume = 0

For Each ws in Worksheets

' Determine the Last Row
LastRow = ws.Cells(Rows.Count, 1).End(xlUp).Row

    For i = 2 To int(LastRow - 1)   

        If Cells(i + 1, 1).Value <> Cells(i, 1).Value Then

            ticker = Cells(i, 1).Value

            closeprice = Cells(i, 6).Value

            yearlychange = closeprice - openprice

            If yearlychange > 0 Then

                percentchange = (yearlychange/openprice)

            Else

                percentchange = (yearlychange/closeprice)

            End If

            Range("H" & ticker_row).Value = ticker

            Range("I" & ticker_row).Value = yearlychange

            Range("J" & ticker_row).Value = percentchange

            Range("K" & ticker_row).Value = stockvolume

            ticker_row = ticker_row + 1     

            nextopenprice = i + 1

            stockvolume = 0

        Else

            stockvolume = stockvolume + Cells(i + 1 , 7).Value

        End If


        If Cells(nextopenprice, 3).Value > 0 Then

            openprice = Cells(nextopenprice, 3).Value

        Else

            MsgBox("End of Data")
            
            Exit Sub 
        
        
        End If

        
    Next i

Next ws

End Sub

        


SELECT Filmes.Nome, Atores.PrimeiroNome,Atores.UltimoNome, ElencoFilme.Papel FROM Filmes
INNER JOIN ElencoFilme ON Filmes.Id = ElencoFilme.IdFilme
INNER JOIN Atores ON ElencoFilme.IdAtor = Atores.Id
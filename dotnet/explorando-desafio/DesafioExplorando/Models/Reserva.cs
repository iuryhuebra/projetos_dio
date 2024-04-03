using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace DesafioExplorando.Models
{
    public class Reserva
    {
        public List<Pessoa> Hospedes { get; set; }
        public Suite Suite { get; set; }
        public int DiasReservados { get; set; }

        public Reserva() { }

        public Reserva(int diasReservados)
        {
            DiasReservados = diasReservados;
        }

        public void CadastrarHospedes(List<Pessoa> hospedes)
        {
            bool verificaCapacidade = hospedes.Count() <= Suite.Capacidade;
            if (verificaCapacidade)
            {
                Hospedes = hospedes;
            }
            else
            {
                throw new ArgumentException("Quantidade de hospedes superior a capacidade da suite.");
            }
        }

        public void CadastrarSuite(Suite suite)
        {
            Suite = suite;
        }

        public int ObterQuantidadeHospedes()
        {
            return Hospedes.Count();
        }

        public decimal CalcularValorDiaria()
        {
            decimal valor = 0;
            valor = Convert.ToDecimal(DiasReservados) * Suite.ValorDiaria;
            bool desconto = DiasReservados >= 10;

            if (desconto)
            {
                valor -= valor * 0.1M;
            }

            return valor;
        }
    }

}
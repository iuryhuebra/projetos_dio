using DesafioPOO.Models;

Console.WriteLine("Iphone:");
Iphone celular1 = new Iphone(numero: "425125", modelo: "X", imei: "111111", memoria: 128);
celular1.Ligar();
celular1.ReceberLigacao();
celular1.InstalarAplicativo(nomeApp: "WhatsApp");

Console.WriteLine("\nNokia:");
Nokia celular2 = new Nokia("214512", "G60", "111111", 32);
celular2.Ligar();
celular2.ReceberLigacao();
celular2.InstalarAplicativo("Instagram");


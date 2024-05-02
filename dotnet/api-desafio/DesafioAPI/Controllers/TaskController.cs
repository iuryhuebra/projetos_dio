using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using DesafioAPI.Context;
using DesafioAPI.Models;
using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore.Storage.ValueConversion;
using Microsoft.IdentityModel.Tokens;

namespace DesafioAPI.Controllers
{
    [ApiController]
    [Route("[controller]")]
    public class TaskController : ControllerBase
    {
        private readonly OrganizerContext _context;

        public TaskController(OrganizerContext context)
        {
        _context = context;
        }

        [HttpGet("{id}")]
        public IActionResult ObterPorId(int id)
        {
            var task = _context.Tasks.Find(id);

            if (task == null)
                return NotFound();

            return Ok(task);
        }

        [HttpGet("ObterTodos")]
        public IActionResult ObterTodos()
        {
            return Ok(_context.Tasks);
        }

        [HttpGet("ObterPorTitulo")]
        public IActionResult ObterPorTitulo(string title)
        {
            var tasks = _context.Tasks.Where(x => x.Title == title);

            return Ok(tasks);
        }

        [HttpGet("ObterPorData")]
        public IActionResult ObterPorData(DateTime date)
        {
            var task = _context.Tasks.Where(x => x.Date.Date == date.Date);
            return Ok(task);
        }

        [HttpGet("ObterPorStatus")]
        public IActionResult ObterPorStatus(EnumStatusTask status)
        {
            var task = _context.Tasks.Where(x => x.Status == status);
            return Ok(task);
        }

        [HttpPost]
        public IActionResult Criar(UserTask task)
        {
            if (task.Date == DateTime.MinValue)
                return BadRequest(new { Erro = "A data da tarefa não pode ser vazia" });

            _context.Tasks.Add(task);
            _context.SaveChanges();
            return CreatedAtAction(nameof(ObterPorId), new { id = task.Id }, task);
        }

        [HttpPut("{id}")]
        public IActionResult Atualizar(int id, UserTask task)
        {
            var taskData = _context.Tasks.Find(id);

            if (taskData == null)
                return NotFound();

            if (task.Date == DateTime.MinValue)
                return BadRequest(new { Erro = "A data da tarefa não pode ser vazia" });

            taskData.Title = task.Title;
            taskData.Description = task.Description;
            taskData.Date = task.Date;
            taskData.Status = task.Status;

            _context.Tasks.Update(taskData);
            _context.SaveChanges();            
            return Ok(taskData);
        }

        [HttpDelete("{id}")]
        public IActionResult Deletar(int id)
        {
            var taskData = _context.Tasks.Find(id);

            if (taskData == null)
                return NotFound();

            _context.Tasks.Remove(taskData);
            _context.SaveChanges();
            return NoContent();
        }

    }
}
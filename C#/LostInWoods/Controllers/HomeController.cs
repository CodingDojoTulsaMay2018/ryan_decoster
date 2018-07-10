using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using LostInWoods.Models;
using LostInWoods.Factory;

namespace LostInWoods.Controllers
{
    public class HomeController : Controller
    {
        private readonly TrailFactory _trailFactory;
        public HomeController(TrailFactory uFactory)
        {
            _trailFactory = uFactory;
        }
        
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            IEnumerable<Trail> AllTrails = _trailFactory.ShowAll();
            foreach(var i in AllTrails) {
                System.Console.WriteLine(i.Id);
            }
            ViewBag.trail = AllTrails;
            return View();
        }

        [HttpGet]
        [Route("NewTrail")]
        public IActionResult NewTrail()
        {
            return View();
        }

        [HttpPost]
        [Route("create")]
        public IActionResult Create(Trail newTrail)
        {
            if(ModelState.IsValid) {
                _trailFactory.Add(newTrail);
                return RedirectToAction("Index");
            }
            else {
                return View("NewTrail", newTrail);
            }
        }

        [HttpGet]
        [Route("trails/{id}")]
        public IActionResult Show(int id)
        {
            // System.Console.WriteLine(ViewBagid);
            ViewBag.dog = _trailFactory.FindByID(id);
            return View();
        }
    }
}

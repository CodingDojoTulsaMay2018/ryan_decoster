using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using Newtonsoft.Json;
using dojodachi.Models;

namespace dojodachi.Controllers
{
    public class HomeController : Controller
    {
        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            Dachi dachi = new Dachi();
            HttpContext.Session.SetObjectAsJson("Dachi", dachi);
            HttpContext.Session.GetObjectFromJson(dachi);
            if (dachi.Fullness <= 0) {
                dachi.Status = "Your Dachi died from starvation!";
                return RedirectToAction("Restart");
            }
            else if (dachi.Happiness <= 0) {
                dachi.Status = "Your Dachi died from being depressed!";
                return RedirectToAction("Restart");
            }
            else {
                return View();
            }
        }

        [HttpGet]
        [Route("feed")]
        public JsonResult Feed()
        {
            Dachi dachi = HttpContext.Session.GetObjectFromJson<Dachi>("Dachi");
            dachi.feed();
            HttpContext.Session.SetObjectAsJson("Dachi", dachi);
            return Json(dachi);
        }

        [HttpGet]
        [Route("play")]
        public JsonResult Play()
        {
            Dachi dachi = HttpContext.Session.GetObjectFromJson<Dachi>("Dachi");
            dachi.play();
            HttpContext.Session.SetObjectAsJson("Dachi", dachi);
            return Json(dachi);
        }

        [HttpGet]
        [Route("work")]
        public JsonResult Work()
        {
            Dachi dachi = HttpContext.Session.GetObjectFromJson<Dachi>("Dachi");
            dachi.work();
            HttpContext.Session.SetObjectAsJson("Dachi", dachi);
            return Json(dachi);
        }

        [HttpGet]
        [Route("sleep")]
        public JsonResult Sleep()
        {
            Dachi dachi = HttpContext.Session.GetObjectFromJson<Dachi>("Dachi");
            dachi.sleep();
            HttpContext.Session.SetObjectAsJson("Dachi", dachi);
            return Json(dachi);
        }

        [HttpGet]
        [Route("restart")]
        public IActionResult Restart() {
            Dachi dachi = HttpContext.Session.GetObjectFromJson<Dachi>("Dachi");
            HttpContext.Session.SetObjectAsJson("Dachi", dachi);
            return View();
        }

        [HttpGet]
        [Route("reset")]
        public IActionResult Reset()
        {
            Dachi dachi = new Dachi();
            HttpContext.Session.Clear();
            return RedirectToAction("Index");
        }

    }
}

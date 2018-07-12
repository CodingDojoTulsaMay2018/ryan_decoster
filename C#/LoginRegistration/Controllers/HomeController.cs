using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using LoginRegistration.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.AspNetCore.Identity;

namespace LoginRegistration.Controllers
{
    
    public class HomeController : Controller
    {
        private YourContext _context;
        public HomeController(YourContext context)
        {
            _context = context;
        }

        [HttpGet]
        [Route("")]
        public IActionResult Index()
        {
            return View();
        }

        [HttpGet]
        [Route("login/user")]
        public IActionResult LoginUser()
        {
            return View("Login");
        }

        [HttpPost]
        [Route("register")]
        public IActionResult Register(User userReg)
        {
            if (ModelState.IsValid){
                PasswordHasher<User> Hasher = new PasswordHasher<User>();
                userReg.Password = Hasher.HashPassword(userReg, userReg.Password);
                _context.Add(userReg);
                _context.SaveChanges();
                return RedirectToAction("Success");
            }
            else {
                return View("Index", userReg);
            }
            
        }

        [HttpPost]
        [Route("login")]
        public IActionResult Login(User userLog)
        {
            var user = _context.Users.SingleOrDefault(u => u.Email == userLog.Email);
            if(user != null && userLog.Password != null)
            {
                var Hasher = new PasswordHasher<User>();
                if(0 != Hasher.VerifyHashedPassword(user, user.Password, userLog.Password))
                {
                    return RedirectToAction("LoginSuccess");
                }
            }
            return View("Login", userLog);
        }

        [HttpGet]
        [Route("success")]
        public IActionResult Success()
        {
            return View();
        }

        [HttpGet]
        [Route("login/success")]
        public IActionResult LoginSuccess() 
        {
            return View();
        }
    }
}

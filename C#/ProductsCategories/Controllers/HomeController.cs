using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.AspNetCore.Http;
using ProductsCategories.Models;
using Microsoft.EntityFrameworkCore;

namespace ProductsCategories.Controllers
{
    public class HomeController : Controller
    {
        private YourContext _context;
        public HomeController(YourContext context)
        {
            _context = context;
        }

        [HttpGet("")]
        public IActionResult Index()
        {
            ViewModel ViewModels = CreateViewModel();

            return View(ViewModels);
        }

        [HttpGet("all")]
        public IActionResult All()
        {
            ViewModel ViewModels = CreateViewModel();

            return View(ViewModels);
        }


        [HttpPost("CreateCategory")]
        public IActionResult CreateCategory(ViewModel FormData)
        {
            if (ModelState.IsValid)
            {
                _context.Add(FormData.Category);
                _context.SaveChanges();
                return Redirect($"categories/{FormData.Category.CategoryId}");
            } else {
                return View("Index", FormData);
            }
            
        }

        [HttpPost("CreateProduct")]
        public IActionResult CreateProduct(ViewModel FormData)
        {
            if (ModelState.IsValid)
            {
                _context.Add(FormData.Product);
                _context.SaveChanges();
                return Redirect($"products/{FormData.Product.ProductId}");
            } else {
                return View("Index", FormData);
            }
        }

        [HttpGet("products/{ProductId}")]
        public IActionResult Product(int ProductId)
        {
            ViewModel pros = new ViewModel()
            {
                Product = _context.Products.SingleOrDefault(w => w.ProductId == ProductId),
                allCategories = _context.Categories.ToList(),
                allProducts = _context.Products
                            .Include(p => p.Categories)
                                .ThenInclude(g => g.Category)
                            .ToList()
            };
            return View(pros);
        }

        [HttpGet("categories/{CategoryId}")]
        public IActionResult Category(int CategoryId)
        {
            ViewModel cats = new ViewModel()
            {
                Category = _context.Categories.SingleOrDefault(w => w.CategoryId == CategoryId),
                allProducts = _context.Products.ToList(),
                allCategories = _context.Categories
                                .Include(c => c.Products)
                                    .ThenInclude(g => g.Product)
                                .ToList()
            };
            return View(cats);
        }

        [HttpPost("ProductToCategory/{CategoryId}")]
        public IActionResult ProductToCategory(ViewModel FormData, int CategoryId)
        {
            Grouping Checker = _context.Categories_Products.SingleOrDefault(p => p.ProductId == FormData.ProductCategory.ProductId && p.CategoryId == CategoryId);
            if(Checker != null)
            {
                TempData["error"] = "The product already exists in the category!";
                return RedirectToAction("Category", CategoryId);
            }
            else{
                if (ModelState.IsValid)
                {
                Grouping newLink = new Grouping()
                {
                    Product = _context.Products.SingleOrDefault(product => product.ProductId == FormData.ProductCategory.ProductId),
                    ProductId = FormData.ProductCategory.ProductId,
                    Category = _context.Categories.SingleOrDefault(category => category.CategoryId == CategoryId),
                    CategoryId = CategoryId
                };
                _context.Categories_Products.Add(newLink);
                _context.SaveChanges();
                return RedirectToAction("Category", CategoryId);
                } else {
                    return View("Category", CategoryId);
                }
            }
        }

        [HttpPost("CategoryToProduct/{ProductId}")]
        public IActionResult CategoryToProduct(ViewModel FormData, int ProductId)
        {
            Grouping Checker = _context.Categories_Products.SingleOrDefault(p => p.ProductId == ProductId && p.CategoryId == FormData.ProductCategory.CategoryId);
            if(Checker != null)
            {
                TempData["error"] = "The category already exists for this product!";
                return RedirectToAction("Product", ProductId);
            }
            else {
                if (ModelState.IsValid)
                {
                Grouping newLink = new Grouping()
                {
                    Product = _context.Products.SingleOrDefault(product => product.ProductId == ProductId),
                    ProductId = ProductId,
                    Category = _context.Categories.SingleOrDefault(category => category.CategoryId == FormData.ProductCategory.CategoryId),
                    CategoryId = FormData.ProductCategory.CategoryId,
                };
                _context.Categories_Products.Add(newLink);
                _context.SaveChanges();
                return RedirectToAction("Product", ProductId);
                } else {
                    return View("Index", FormData);
                }
            }
        }

        private ViewModel CreateViewModel()
        {
            ViewModel ViewModels = new ViewModel()
            {
                allProducts = _context.Products
                .Include(Product => Product.Categories)
                    .ThenInclude(Categories => Categories.Product)
                .ToList(),
                allCategories = _context.Categories
                .Include(Category => Category.Products)
                    .ThenInclude(Products => Products.Category)
                .ToList(),
            };
            return ViewModels;
        }
    }
}
